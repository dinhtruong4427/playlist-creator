import { ImageBox } from "../basic_elements/ImageBox";
import { SongLabel } from "../basic_elements/SongLabel.js";
import './SmallSongCard.css';

export function SmallSongCard({ src, alt="Album Cover", title, artist }) {
    const container = document.createElement('div');
    container.className = 'small-song-card';
    
    let imageURL = ''
    if (src) {
        imageURL = src.replace("http://", "https://");
        imageURL = imageURL.replace(/100x100bb/, "500x500bb");
    }

    const imageBox = ImageBox({ src, alt , width: '75px', height: '75px' });
    const songLabel = SongLabel({ title, artist, size: 'medium', orientation: 'left' });
    
    container.appendChild(imageBox);
    container.appendChild(songLabel);
    
    return container;
}