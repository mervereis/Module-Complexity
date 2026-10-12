/**
 * Finds common items between two arrays.
 *
 * Time Complexity: O(n * m)
 * Space Complexity: O(n)
 * Optimal Time Complexity: O(n + m)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */

export const findCommonItems = (firstArray, secondArray) => [
  ...new Set(firstArray.filter((item) => secondArray.includes(item))),
];

// Time complexity is O(n * m) because for each item in the first array,
// includes() may search through the entire second array.

// Space complexity is O(n) because filter() creates a new array
// and Set stores unique common items.

// Optimal time complexity is O(n + m) because using Sets
// allows us to check for common items more efficiently.
export function findCommonItems(firstArray, secondArray) {
  const secondSet = new Set(secondArray);
  const commonItems = new Set();

  for (const item of firstArray) {
    if (secondSet.has(item)) {
      commonItems.add(item);
    }
  }

  return [...commonItems];
}

// Time complexity: O(n + m)
// Space complexity: O(n + m)
// Optimal time complexity: O(n + m)
