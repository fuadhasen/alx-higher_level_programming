#!/usr/bin/node

const arr = process.argv.slice(2);
if (arr.length === 0) {
  console.log('0');
} else if (arr.length === 1) {
  console.log('0');
} else {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (arr[j] > arr[j + 1]) {
        const temp = arr[j + 1];
        arr[j + 1] = arr[j];
        arr[j] = temp;
      }
    }
  }
  console.log(arr[arr.length - 2]);
}
