// Wait for DOM to load
$(function () {
  $("#navbarToggle").blur(function () {
    var screenWidth = window.innerWidth;
    if (screenWidth < 768) {
      $("#collapsable-nav").collapse('hide');
    }
  });
});

(function (global) {

  var dc = {};

  // URLs & snippet paths
  var homeHtmlUrl = "snippets/home-snippet.html";
  var allCategoriesUrl = "https://davids-restaurant.herokuapp.com/categories.json";
  var categoriesTitleHtml = "snippets/categories-title-snippet.html";
  var categoryHtml = "snippets/category-snippet.html";
  var menuItemsUrl = "https://davids-restaurant.herokuapp.com/menu_items.json?category=";
  var menuItemsTitleHtml = "snippets/menu-items-title.html";
  var menuItemHtml = "snippets/menu-item.html";

  // Helper: insert HTML
  var insertHtml = function (selector, html) {
    document.querySelector(selector).innerHTML = html;
  };

  // Show loading spinner
  var showLoading = function (selector) {
    var html = "<div class='text-center'>";
    html += "<img src='images/ajax-loader.gif'></div>";
    insertHtml(selector, html);
  };

  // Replace {{propName}} in string with propValue
  var insertProperty = function (string, propName, propValue) {
    var propToReplace = "{{" + propName + "}}";
    return string.replace(new RegExp(propToReplace, "g"), propValue);
  };

  // Switch active button in navbar
  var switchMenuToActive = function () {
    var classes = document.querySelector("#navHomeButton").className;
    classes = classes.replace(new RegExp("active", "g"), "");
    document.querySelector("#navHomeButton").className = classes;

    classes = document.querySelector("#navMenuButton").className;
    if (classes.indexOf("active") === -1) {
      classes += " active";
      document.querySelector("#navMenuButton").className = classes;
    }
  };

  // On page load
  document.addEventListener("DOMContentLoaded", function () {
    showLoading("#main-content");
    $ajaxUtils.sendGetRequest(
      allCategoriesUrl,
      buildAndShowHomeHTML,
      true // Parse JSON
    );
  });

  // Build home HTML
  function buildAndShowHomeHTML(categories) {
    $ajaxUtils.sendGetRequest(homeHtmlUrl, function (homeHtml) {
      var chosenCategoryShortName = "'" + chooseRandomCategory(categories).short_name + "'";
      var homeHtmlToInsert = insertProperty(homeHtml, "randomCategoryShortName", chosenCategoryShortName);
      insertHtml("#main-content", homeHtmlToInsert);
    }, false);
  }

  // Pick random category
  function chooseRandomCategory(categories) {
    var randomIndex = Math.floor(Math.random() * categories.length);
    return categories[randomIndex];
  }

  // Load all categories view
  dc.loadMenuCategories = function () {
    showLoading("#main-content");
    $ajaxUtils.sendGetRequest(allCategoriesUrl, buildAndShowCategoriesHTML);
  };

  // Load menu items of a category
  dc.loadMenuItems = function (categoryShort) {
    showLoading("#main-content");
    $ajaxUtils.sendGetRequest(menuItemsUrl + categoryShort, buildAndShowMenuItemsHTML);
  };

  // Build categories HTML
  function buildAndShowCategoriesHTML(categories) {
    $ajaxUtils.sendGetRequest(categoriesTitleHtml, function (categoriesTitle) {
      $ajaxUtils.sendGetRequest(categoryHtml, function (categorySnippet) {
        switchMenuToActive();
        var finalHtml = buildCategoriesViewHtml(categories, categoriesTitle, categorySnippet);
        insertHtml("#main-content", finalHtml);
      }, false);
    }, false);
  }

  function buildCategoriesViewHtml(categories, categoriesTitleHtml, categoryHtml) {
    var finalHtml = categoriesTitleHtml + "<section class='row'>";
    for (var i = 0; i < categories.length; i++) {
      var html = categoryHtml;
      html = insertProperty(html, "name", categories[i].name);
      html = insertProperty(html, "short_name", categories[i].short_name);
      finalHtml += html;
    }
    finalHtml += "</section>";
    return finalHtml;
  }

  // Build menu items HTML
  function buildAndShowMenuItemsHTML(categoryMenuItems) {
    $ajaxUtils.sendGetRequest(menuItemsTitleHtml, function (menuItemsTitle) {
      $ajaxUtils.sendGetRequest(menuItemHtml, function (menuItemSnippet) {
        switchMenuToActive();
        var finalHtml = buildMenuItemsViewHtml(categoryMenuItems, menuItemsTitle, menuItemSnippet);
        insertHtml("#main-content", finalHtml);
      }, false);
    }, false);
  }

  function buildMenuItemsViewHtml(categoryMenuItems, menuItemsTitleHtml, menuItemHtml) {
    menuItemsTitleHtml = insertProperty(menuItemsTitleHtml, "name", categoryMenuItems.category.name);
    menuItemsTitleHtml = insertProperty(menuItemsTitleHtml, "special_instructions", categoryMenuItems.category.special_instructions);

    var finalHtml = menuItemsTitleHtml + "<section class='row'>";
    var menuItems = categoryMenuItems.menu_items;
    var catShortName = categoryMenuItems.category.short_name;

    for (var i = 0; i < menuItems.length; i++) {
      var html = menuItemHtml;
      html = insertProperty(html, "short_name", menuItems[i].short_name);
      html = insertProperty(html, "catShortName", catShortName);
      html = insertItemPrice(html, "price_small", menuItems[i].price_small);
      html = insertItemPortionName(html, "small_portion_name", menuItems[i].small_portion_name);
      html = insertItemPrice(html, "price_large", menuItems[i].price_large);
      html = insertItemPortionName(html, "large_portion_name", menuItems[i].large_portion_name);
      html = insertProperty(html, "name", menuItems[i].name);
      html = insertProperty(html, "description", menuItems[i].description);

      if (i % 2 !== 0) html += "<div class='clearfix visible-lg-block visible-md-block'></div>";
      finalHtml += html;
    }
    finalHtml += "</section>";
    return finalHtml;
  }

  // Append price
  function insertItemPrice(html, pricePropName, priceValue) {
    if (!priceValue) return insertProperty(html, pricePropName, "");
    priceValue = "$" + priceValue.toFixed(2);
    return insertProperty(html, pricePropName, priceValue);
  }

  // Append portion name
  function insertItemPortionName(html, portionPropName, portionValue) {
    if (!portionValue) return insertProperty(html, portionPropName, "");
    portionValue = "(" + portionValue + ")";
    return insertProperty(html, portionPropName, portionValue);
  }

  global.$dc = dc;

})(window);
