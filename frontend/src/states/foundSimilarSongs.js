let foundSimilarSongs = [];
const listeners = new Set();

export function getSimilarSongs() {
  return foundSimilarSongs;
}

export function addSimilarSong(song) {
  foundSimilarSongs.append(song);
  listeners.forEach(fn => fn(song));
}

export function clearSimilarSongs() {
  foundSimilarSongs = []
  return () => listeners.delete(fn);
}