import './numDropdown.css';

export function Dropdown(){
    const dropdown = document.createElement('select');
    dropdown.className = 'dropdown';

    const options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];

    options.forEach(opt => {
        const option = document.createElement('option');
        option.value = opt.toLowerCase();
        option.textContent = opt;
        dropdown.appendChild(option);
    });
    dropdown.addEventListener('change', () => {
        console.log('Selected:', dropdown.value);
    });

    return dropdown;
}