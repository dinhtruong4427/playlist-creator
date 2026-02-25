import './BoxLabel.css';

export function BoxLabel({ title, subtitle, orientation = 'center' }) {
    const container = document.createElement('div');
    container.className = 'label-container';

    const titleEl = document.createElement('div');
    titleEl.className = 'box-title';
    titleEl.textContent = title;
    container.appendChild(titleEl);

    const subtitleEl = document.createElement('div');
    subtitleEl.className = 'box-subtitle';
    subtitleEl.textContent = subtitle;
    if (subtitleEl.textContent) {
        container.appendChild(subtitleEl);
    }

    if (orientation === 'left') {
        container.classList.add('left-align');
    }

    function changeTitle(newTitle, removeSubtitle = false) {
        
        container.classList.add('retracted');
        titleEl.textContent = newTitle;
        setTimeout(() => {
            container.classList.remove('retracted');
        }, 400);
        if (removeSubtitle && subtitleEl) {
            container.removeChild(subtitleEl);
        }
    }

    return {container, changeTitle};
}