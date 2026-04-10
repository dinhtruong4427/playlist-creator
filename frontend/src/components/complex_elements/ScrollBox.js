import './ScrollBox.css';

export function ScrollBox() {
    const scrollContainer = document.createElement('div');
    scrollContainer.className = 'scroll-container';

    const container = document.createElement('div');
    container.className = 'scroll-box';

    scrollContainer.appendChild(container);

    const spinner = document.createElement('div')
    spinner.className = 'spinner';
    scrollContainer.appendChild(spinner);

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

    function showSpinner() {
        console.log("Showing spinner")
        spinner.style.display = 'block';
    }

    function hideSpinner() {
        spinner.classList.add('fade-out');
        setTimeout(() => {
            spinner.style.display = 'none';
            spinner.classList.remove('fade-out');
        }, 400);
    }

    return {
        scrollContainer,
        container,
        addItem,
        clearScroll,
        addItemAnimated,
        showSpinner,
        hideSpinner
    };
}