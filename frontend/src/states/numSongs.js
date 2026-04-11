let numSongs = 5;
const listeners = new Set();

export function getNumSongs() {
  return numSongs;
}

export function setNumSongs(num) {
  numSongs = num;
  listeners.forEach(fn => fn(song));
}
