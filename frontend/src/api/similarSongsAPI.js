let controller; // keeps track of the current similarity request

/**
 * Fetch similar songs based on a preview URL + song name
 *
 * @param {Object} params
 * @param {string} params.songUrl   - Apple previewUrl
 * @param {string} params.songName  - Song name (used for embedding)
 * @param {number} [params.topN=5]  - Number of similar songs to return
 * @returns {Promise<Array<{ id: int, title: str, artist: str, albumArtwork: str, previewUrl: str }>>}
 */
export async function getSimilarSongs({ songId, topN = 5 }) {
  // Cancel previous request if it exists
  if (controller) {
    controller.abort();
  }

  controller = new AbortController();
  const signal = controller.signal;

  const params = new URLSearchParams({
    song_id: songId,
    top_n: topN,
  });

  try {
    const res = await fetch(`/api/similar?${params.toString()}`, { signal });

    if (!res.ok) {
      const text = await res.text();
      throw new Error(`Similar songs failed (${res.status}): ${text}`);
    }

    const resultJSON = await res.json();
    console.log("Raw similar songs response:", resultJSON);

    return resultJSON.results;
  } catch (err) {
    if (err.name === "AbortError") {
      // Request was intentionally cancelled
      return [];
    }

    console.error("Similar songs error:", err);
    return [];
  }
}
