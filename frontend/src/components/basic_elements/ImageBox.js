import './ImageBox.css';

export function ImageBox({
  src,
  alt = '',
  width = '250px',
  height = '250px',
  rounded = true,
}) {
  const container = document.createElement('div');
  container.className = 'image-box';

  container.style.width = width;
  container.style.height = height;

  if (!rounded) {
    container.classList.add('square');
  }

  const img = document.createElement('img');
  img.src = src;
  img.alt = alt;

  container.setSrc = (newSrc) => {
    img.src = newSrc;
  };

  container.appendChild(img);
  return container;
}
