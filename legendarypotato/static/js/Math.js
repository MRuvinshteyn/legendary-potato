const WolframAlphaAPI = require('wolfram-alpha-api');
const waApi = WolframAlphaAPI('DEMO-APPID');

waApi.getFull('sin x').then(console.log).catch(console.error);
// { success: true, error: false, numpods: 13, datatypes: '', ...

waApi.getFull('F9TVlu5AmVzL').then(console.log).catch(console.error);
// { success: false, error: false, numpods: 0, datatypes: '', ...

waApi.getFull('sin(x)').then((queryresult) => {
  const pods = queryresult.pods;
  const output = pods.map((pod) => {
    const subpodContent = pod.subpods.map(subpod =>
      `  <img src="${subpod.img.src}" alt="${subpod.img.alt}">`
    ).join('\n');
    return `<h2>${pod.title}</h2>\n${subpodContent}`;
  }).join('\n');
  console.log(output);
}).catch(console.error);