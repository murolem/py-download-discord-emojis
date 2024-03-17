# py-download-discord-emojis

A little python script for downloading discord emojis.

# Usage

1. Go to the web version of discord, open the emoji popup.
2. Open devtools, select a container element from which you want to download emojis (with devtools select tool).
3. Run this script to generate the output needed to download the emojis:

```js
(() => {
    const container = $0;
    const images = container.querySelectorAll("img");
    const urls = [...images].reduce((accum, img) => {
        accum.push([img.src, img.alt]);
        return accum;
    }, []);
    console.log(JSON.stringify(urls, null, 4));
})();
```

Please note that the discord seem to display only the visible emojies, so if you want to copy a lot of them you would have to scroll to the ones not currently visible and run the script again.

Don't worry about duplicates though - they will get overridden anyway.

4. Copy the output.
5. Paste the output to the script `urls` var.
6. Run `pipenv install` to install the env with dependencies. This requires `pipenv` to be installed.
7. Select the installed environment (bottom right in the vs code).
8. Run `pipenv run python d.py` to start the download.
