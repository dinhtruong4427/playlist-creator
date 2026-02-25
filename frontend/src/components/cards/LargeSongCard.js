import { ImageBox } from "../basic_elements/ImageBox";
import { SongLabel } from "../basic_elements/SongLabel.js";
import './largeSongCard.css';

export function LargeSongCard({ src, alt="Album Cover", title, artist }) {
    const container = document.createElement('div');
    container.className = 'large-song-card';
    
    const imageBox = ImageBox({ src, alt });
    const songLabel = SongLabel({ title, artist });
    songLabel.classList.add('medium');
    
    container.appendChild(imageBox);
    container.appendChild(songLabel);

    
    function updateSong(song) {
        if (!song) return;
        console.log(song.albumArtwork)

        let imageURL  = song.albumArtwork.replace("http://", "https://")
        imageURL = imageURL.replace(/100x100bb/, "500x500bb");

        if (song.albumArtwork) {
            imageBox.setSrc(imageURL);
        }

        if (song.title || song.artist) {
        songLabel.update({
            title: song.title,
            artist: song.artist,
        });
        }
    }

    return {container, updateSong};
}