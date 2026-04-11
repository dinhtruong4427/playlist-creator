import './numDropdown.css';
import { setNumSongs } from '../../states/numSongs';

export function Dropdown() {
    const wrapper = document.createElement('div');
        wrapper.className = 'dropdown-wrapper';

    const dropdownLabel = document.createElement('div');
        dropdownLabel.className = 'dropdown-label'
        dropdownLabel.textContent = '#:'

    const trigger = document.createElement('div');
        trigger.className = 'dropdown-trigger';
        trigger.textContent = '1';

    const grid = document.createElement('div');
        grid.className = 'num-grid hidden';

    const options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'];

    options.forEach(opt => {
        const item = document.createElement('div');
        item.className = 'num-grid-item';
        item.textContent = opt;

        item.addEventListener('click', () => {
            grid.querySelectorAll('.num-grid-item').forEach(i => i.classList.remove('selected'));
            item.classList.add('selected');
            trigger.textContent = opt;
            setNumSongs(opt);
            grid.classList.add('hidden');
        });

        grid.appendChild(item);
    });

    trigger.addEventListener('click', (e) => {
        e.stopPropagation();
        grid.classList.toggle('hidden');
    });

    document.addEventListener('click', () => grid.classList.add('hidden'));

    wrapper.appendChild(dropdownLabel)
    wrapper.appendChild(trigger);
    wrapper.appendChild(grid);

    return wrapper;
}