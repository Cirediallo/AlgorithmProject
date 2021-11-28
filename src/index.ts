import { createInterface } from 'readline';
import { promisify } from 'util';
import * as cliSelect from 'cli-select';

function question(text): Promise<string> {
  return new Promise((resolve) => {
    const rl = createInterface({
      input: process.stdin,
      output: process.stdout,
    });

    rl.question(text, (value) => {
      rl.close();
      rl.removeAllListeners();
      resolve(value);
    });
  });
}

async function start() {
  console.log('Please choose between the following input modes:');

  const inputMode = await cliSelect({ values: ['Ip', 'Ir'] });

  let instance = [];

  if (inputMode?.value == 'Ip') {
    const p = parseInt((await question('Enter a value for p: ')) as string);

    if (p > 0) {
      // Create an array composed of 4 * p 1s
      // 2 * p * (p - 1) 2s
      // and 1 2p
      const ones = Array(4 * p).fill(1);
      const twos = Array(2 * p * (p - 1)).fill(2);
      instance = [...ones, ...twos, 2 * p];

      console.log(instance);
    } else {
      console.log('p must be a positive number');
    }
  }

  // No input mode was chosen
  else {
    console.error('It seems an error has occured while choosing the input mode.');
  }
}

(async () => {
  start();
})();
