import { BuildButton } from "../basic_elements/buildButton.js";
import { Dropdown } from "../basic_elements/numDropdown.js";
import './BuildPlaylistCard.css';

export function BuildPlaylistCard({onClick}) {
    const container = document.createElement('div');
    container.className = 'playlist-card';
    
    const dropdownLabel = document.createElement('div');
    dropdownLabel.className = 'dropdown-label'
    dropdownLabel.textContent = '#:'


    const dropdown = Dropdown()
    const buildButton = BuildButton({label:'Build Playlist', onClick: onClick})
    
    buildButton.classList.add('expanded')
    container.appendChild(buildButton);
    container.appendChild(dropdownLabel)
    container.appendChild(dropdown);
    
    return container;
}