console.log('Gabster!');
let beers;
(async function () {
    const res = await axios.get('https://api.sampleapis.com/beers/ale');
    beers = res.data;
})();
