//Elements
import { Sidebar } from '../components/complex_elements/Sidebar.js';
import { SearchBar } from '../components/complex_elements/SearchBar.js';
import { ScrollBox } from '../components/complex_elements/ScrollBox.js';
import { BuildButton } from '../components/basic_elements/buildButton.js';
import { LargeSongCard } from '../components/cards/largeSongCard.js';
import { SmallSongCard } from '../components/cards/SmallSongCard.js';
import { BoxLabel } from '../components/basic_elements/BoxLabel.js';
//States
import { getSelectedSong, setSelectedSong, subscribeSelectedSong } from '../states/singleSelectedSong.js';
//APIs
import { searchSongs } from '../api/searchAPI.js';
import { getSimilarSongs } from '../api/similarSongsAPI.js';
import './home.css'

function debounce(fn, delay = 300) {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => fn(...args), delay);
  };
}

export function HomePage(navigate) {
    const container = document.createElement('div');
    container.className = 'home-page'

    const boxWrapper = document.createElement('div');
    boxWrapper.className = 'box-wrapper';

    const box = document.createElement('div');
    box.className = 'box';

    const expandedBox = document.createElement('div');
    expandedBox.className = 'expanded-box';

    const scrollBox = ScrollBox();
    const boxTitle = BoxLabel({title: "Song Suggestions", 
                            subtitle: "Select a song and find similar tracks", 
                            orientation: 'middle'});
    const expandedBoxTitle = BoxLabel({title: "Similar Songs:", orientation: 'left'});
    
    expandedBox.appendChild(expandedBoxTitle.container);
    expandedBox.appendChild(scrollBox.scrollContainer);


    const songs = ['15 Steps', 
        'Body Snatchers',
        'Nude', 
        'Weird Fishes / Arpeggi',
        'All I Need', 
        'Faust Arp', 
        'Reckoner'];

    const mainSongCard = LargeSongCard({
        src: '/In_Rainbows.jpg',
        title: 'In Rainbows',
        artist: 'Radiohead',
    });

    const buildButton = BuildButton({
        label: 'Build Playlist',
        onClick: debounce(async (query) => {
            console.log('Build Playlist button clicked');
            box.classList.add('expanded');
            expandedBox.classList.add('expanded');
            //boxTitle.changeTitle('Selected Song:', true);

            let currentSelectedSong = getSelectedSong();

            let similarSongs = await getSimilarSongs({
                songId: currentSelectedSong.id,
                topN: 5,
            })

            console.log("Similar songs fetched:", similarSongs);

            setTimeout(() => {}, 400)
            for (let i = 0; i < 5; i++) {
                scrollBox.addItemAnimated(SmallSongCard({
                    src: similarSongs[i].albumArtwork,
                    title: similarSongs[i].title,
                    artist: similarSongs[i].artist,
                }), i * 200);
            }
        })
    });

    
    const sidebar = Sidebar(navigate);
    const searchBar = SearchBar({
        placeholder: 'Search songs...',
        data: [],
        onSelect: (item) => {
            console.log("Item selected:", item);
            mainSongCard.container.classList.remove('expanded');
            buildButton.classList.remove('expanded');
            box.classList.remove('expanded');
            expandedBox.classList.remove('expanded');
            setSelectedSong(item)
            mainSongCard.updateSong(item);
            setTimeout(() => {
                mainSongCard.container.classList.add('expanded');
                buildButton.classList.add('expanded');
            }, 400);
        },
        onInput: debounce(async (query) => {
            try {
                if (query.length < 2) return;
                console.log("Searching for:", query);
                const results = await searchSongs(query);
                console.log("Search results:", results);

                searchBar.setData(results); // assuming your SearchBar has a setData method
            } catch (err) {
                console.error(err);
            }
        }, 400)
});

    container.appendChild(sidebar);

    box.appendChild(boxTitle.container);
    box.appendChild(searchBar.element); //note, change everything to element
    box.appendChild(mainSongCard.container);
    box.appendChild(buildButton);

    boxWrapper.appendChild(box);
    boxWrapper.appendChild(expandedBox);

    container.appendChild(boxWrapper);
    return container;
}
