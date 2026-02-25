import { Sidebar } from '../components/complex_elements/Sidebar.js';
import './contact.css'
export function ContactPage(navigate) {
    const container = document.createElement('div');
    container.className = 'contact-page'

    const box = document.createElement('div');
    box.className = 'box';

    const items = ['Emily', 'is', 'a', 'gift', 'of', 'a', 'soul']

    const sidebar = Sidebar(navigate);

    const ul = document.createElement('ul');
    items.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item
        ul.appendChild(li);
    });

    container.appendChild(sidebar);
    box.appendChild(ul);
    container.appendChild(box);
    return container;
}