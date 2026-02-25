// state/selectedSong.js
let selectedSong = null;
const listeners = new Set();

export function getSelectedSong() {
  return selectedSong;
}

export function setSelectedSong(song) {
  selectedSong = song;
  listeners.forEach(fn => fn(song));
}

export function subscribeSelectedSong(fn) {
  listeners.add(fn);
  return () => listeners.delete(fn);
}
