import './ScrollBox.css';

export function ScrollBox() {
    const scrollContainer = document.createElement('div');
    scrollContainer.className = 'scroll-container';

    const container = document.createElement('div');
    container.className = 'scroll-box';

    scrollContainer.appendChild(container);

    function addItem(element) {
        container.appendChild(element);
        container.scrollTop = container.scrollHeight
    }

    function clearScroll() {
        container.replaceChildren();
    }

    function addItemAnimated(element, delay = 0) {
        container.appendChild(element);
        container.scrollTop = container.scrollHeight;
        
        setTimeout(() => {
            requestAnimationFrame(() => {
            element.classList.add('expanded');
            });
        }, delay);
    }

    return {
        scrollContainer,
        container,
        addItem,
        clearScroll,
        addItemAnimated
    };
}