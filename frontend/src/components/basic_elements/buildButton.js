import './buildButton.css';

export function BuildButton({ label = 'Generate', onClick }) {
  const button = document.createElement('button');
  button.className = 'build-button';
  button.textContent = label;

  if (onClick) {
    button.addEventListener('click', onClick);
  }

  return button;
}
