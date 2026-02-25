import { navigate } from './router.js';

const app = document.createElement('div');
app.id = 'app';
document.body.appendChild(app);

navigate('home');

