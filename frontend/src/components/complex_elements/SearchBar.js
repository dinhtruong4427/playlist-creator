import './SearchBar.css';

export function SearchBar({
  placeholder = 'Search...',
  data = [],
  onSelect = () => {},
  onInput = () => {},
}) {
  const wrapper = document.createElement('div');
  wrapper.className = 'search-wrapper';

  const input = document.createElement('input');
  input.className = 'search-input';
  input.placeholder = placeholder;

  const list = document.createElement('ul');
  list.className = 'search-results';

  let filtered = [];
  let activeIndex = -1;
  let requestId = 0;


  function render() {
    list.innerHTML = '';

    filtered.forEach((item, index) => {
      const li = document.createElement('li');
      li.textContent = item.title + ' - ' + item.artist;
      li.className = 'search-item';

      if (index === activeIndex) {
        li.classList.add('active');
      }

      li.onclick = () => {
        onSelect(item);
        input.value = item.title;
        clear();
      };

      list.appendChild(li);
    });
  }

  function clear() {
    filtered = [];
    activeIndex = -1;
    list.innerHTML = '';
  }

  input.addEventListener('input', async () => {
    const q = input.value.toLowerCase();
    //const currentRequest = ++requestId;

    if (!q) {
      clear();
      return;
    }

    try {
      onInput(q);

      activeIndex = -1;
      render();
    } catch (err) {
      console.error('Search failed:', err);
      clear();
    }
  });

  input.addEventListener('keydown', (e) => {
    if (!filtered.length) return;

    if (e.key === 'ArrowDown') {
      activeIndex = (activeIndex + 1) % filtered.length;
      render();
    }

    if (e.key === 'ArrowUp') {
      activeIndex =
        (activeIndex - 1 + filtered.length) % filtered.length;
      render();
    }

    if (e.key === 'Enter' && activeIndex >= 0) {
      const item = filtered[activeIndex];
      onSelect(item);
      input.value = getLabel(item);
      clear();
    }
  });

  function setData(newData = []) {
    filtered = newData;
    activeIndex = -1;
    render();
  }

  wrapper.append(input, list);

  return {
    element: wrapper,
    setData,
    clear,
  };
}
