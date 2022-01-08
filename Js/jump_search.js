function jump_search(arr, find) {
  let length = arr.length;

  let step = Math.sqrt(length);

  let prev = 0;

  while (arr[Math.floor(Math.min(step, length) - 1)] < find) {
    prev = Math.floor(step);
    step += Math.sqrt(length);

    if (prev >= find) {
      return -1;
    }
  }

  while (arr[prev] < find) {
    prev += 1;

    if (prev == Math.min(step, length)) {
      return -1;
    }
  }

  if (arr[prev] == find) {
    return prev;
  }

  return -1;
}

let arr = new Array(10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47);
let find = 22;

let position = jump_search(arr, find);
position == -1
  ? console.log("Element was not present in given list.")
  : console.log("Element is presented at " + (position + 1) + " position.");
