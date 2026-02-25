import './Sidebar.css';

export function Sidebar(navigate) {
  const menuItems = [
        { label: 'Home', route: 'home' },
        { label: 'Stats', route: 'stats' },
        { label: 'Contact', route: 'contact' },
    ]

  const sidebar = document.createElement('div');
  sidebar.className = 'sidebar';

  menuItems.forEach(item => {
    const menuItem = document.createElement('div');
    menuItem.className = 'sidebar-item';
    menuItem.textContent = item.label;

    if (item.route) {
      menuItem.addEventListener('click', () => {
        navigate(item.route);
      });
    }

    sidebar.appendChild(menuItem);
  });

  return sidebar;
}
