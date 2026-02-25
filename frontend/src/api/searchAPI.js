let controller; // keeps track of the current request

export async function searchSongs(query) {
  // Cancel previous request if it exists
  if (controller) {
    controller.abort();
  }

  controller = new AbortController();
  const signal = controller.signal;

  try {
    const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`, { signal });

    if (!res.ok) {
      const text = await res.text(); // helpful for debugging
      throw new Error(`Search failed (${res.status}): ${text}`);
    }

    const resultJSON = await res.json();
    console.log("Raw search response:", resultJSON);
    return resultJSON.results;
  } catch (err) {
    if (err.name === "AbortError") {
      // Request was aborted — silently ignore
      return [];
    }
    console.error("Search error:", err);
    return [];
  }
}
