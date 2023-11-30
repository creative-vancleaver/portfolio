/**
 * @jest-environment jsdom
 */


// import $ from 'jquery'
// import { activeNavLink } from '../../js/base'
//  import $ from 'jquery';
//  import { activeNavLink } from '../base.js';
//  import { TextEncoder, TextDecoder } from 'util';
//  Object.assign(global, { TextDecoder, TextEncoder });
//  import JSDOM from 'jsdom';

const $ = require('jquery');
const activeNavLink = require('../static/js/base.js');
const { TextEncoder } =  require('text-encoding');

// global.TextEncoder = TextEncoder;
Object.assign(global, { TextEncoder });
const { JSDOM } = require('jsdom');


// const $ = require('jquery');
// const activeNavLink = require('../../js/base');

// const JSDOM = require('jsdom');

// global.TextEncoder = TextEncoder;

// describe('Base', () => {
//   beforeEach(() => {
    
//   })
// })



// test('addEventListener to button', () => {
//   const $myButton = document.querySelectorAll('.nav-link');

//   // activeNavLink($myButton);

//   expect($myButton)
// });

const dom = new JSDOM('<!DOCTYPE html><html><body></body></html>');
global.document = dom.window.document;
global.window = dom.window;

// import { activeNavLink } from '../base.js';

describe('activeNavLink', () => {
  let navLinks;

  beforeEach(() => {
    document.body.innerHTML = `
      <div class='nav-link'></div>
      <div class='nav-link'></div>
    `;

    navLinks = document.querySelectorAll('.nav-link');

    activeNavLink();
  });

  test('clicking a nav link toggles the "active" class', () => {
    const firstNavLink = navLinks[0];
    firstNavLink.click();

    expect($(firstNavLink).hasClass('active')).toBe(true);

    firstNavLink.click();

    expect($(firstNavLink).hasClass('active')).toBe(false);
  })

})