const add = require('../static/js/add');

test('proerly adds 2 numbers', () => {
  expect(add(1, 2)).toBe(3)
})