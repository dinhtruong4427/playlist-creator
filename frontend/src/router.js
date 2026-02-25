import { HomePage } from './pages/home.js';
import { ContactPage } from './pages/contact.js';
import { StatsPage } from './pages/stats.js';

const routes = {
  home: HomePage,
  contact: ContactPage,
  stats: StatsPage
};

export function navigate(route) {
  const app = document.getElementById('app');
  app.innerHTML = '';
  app.appendChild(routes[route](navigate));
}
