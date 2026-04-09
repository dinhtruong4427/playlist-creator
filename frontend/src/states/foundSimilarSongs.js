let foundSimilarSongs = [];
const listeners = new Set();

export function getSimilarSongs() {
  return foundSimilarSongs;
}

export function addSimilarSong(song) {
  selectedSong = song;
  listeners.forEach(fn => fn(song));
}

export function subscribeSelectedSong(fn) {
  listeners.add(fn);
  return () => listeners.delete(fn);
}