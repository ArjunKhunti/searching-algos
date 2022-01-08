function search(arr, find) {
  let length = arr.length;
  let i = 0;
  for (i = 0; i < length; i++) {
    if (arr[i] == find) {
      return i;
    }
  }
  return -1;
}

let arr = [12, 45, 76, 34, 23, 87, 26, 85];
let find = 85;

let position = search(arr, find);

position == -1
  ? console.log("Element is not present in given list.")
  : console.log("Element is present at " + (position + 1) + " position.");
