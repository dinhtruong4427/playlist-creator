import './SongLabel.css';

export function SongLabel({ title,
  artist, 
  size = 'large', 
  orientation = 'centered' 
  }) {
  const container = document.createElement('div');
  container.className = 'song-label';

  const titleEl = document.createElement('div');
  titleEl.className = 'song-title';
  titleEl.textContent = title;

  const artistEl = document.createElement('div');
  artistEl.className = 'song-artist';
  artistEl.textContent = artist;

  container.appendChild(titleEl);
  container.appendChild(artistEl);
  
  if (size === 'medium') {
    container.classList.add('medium');
  }
  if (orientation === 'left') {
    container.classList.add('left');
  }

  container.update = ({ title, artist }) => {
    if (title) titleEl.textContent = title;
    if (artist) artistEl.textContent = artist;
  };

  return container;
}
