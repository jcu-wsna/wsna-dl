import itemsjs from "itemsjs";
import { ref } from "vue";

let itemsjsInstance;
const filteredDocList = ref([]);
let fullDocList = [];

//  selectedFilters:
//  keys are filter categories, values are lists of options in the category
//  that have been selected. Don't need to include categories with no
//  selections.
let selectedFilters = {};
let searchQuery = "";

// this structure is required by itemsjs
const filterConfig = {
  sortings: {
    name_asc: {
      field: "Title",
      order: "asc",
    },
    year_name_asc: {
      field: ["Year", "Title"],
      order: ["desc", "asc"],
    },
  },
  // what fields the search indexes
  searchableFields: [
    "Title",
    "ID",
    "Authors",
    "Year",
    "JournalOrPublisher",
    "Abstract_Description",
  ],
  // What facets (filter categories) are used on the side
  // See https://github.com/itemsapi/itemsjs/blob/master/docs/configuration.md
  //   for more information.
  // size is the number of values provided for this filter
  //     doco doesn't say how accurate it needs to be
  aggregations: {
    Access_Rights: { title: "Access Rights", size: 2 },
    Habitat_type: { title: "Habitat Type", size: 13 },
    Category: { title: "Publication Type", size: 6 },
    JournalOrPublisher: { title: "Journal or Publisher", size: 45 },
    Year: { title: "Year of Publication", size: 25 },
  },
};

// translating from facet -> category and bucket -> option
export function getFullDocList(docList) {
  fullDocList = docList;
  itemsjsInstance = itemsjs(fullDocList, filterConfig);
  selectedFilters = resetFilters();
  selectedFilters = [];
  searchQuery = "";

  filteredDocList.value = itemsjsInstance.search({
    per_page: 100,
    query: searchQuery,
    filters: selectedFilters,
    sort: "year_name_asc", // defined in filterConfig.sortings
    isExactSearch: true,
  });

  return filteredDocList.value;
}

// function resetFilters() {
//   let newFilters = {};
//   Object.keys(filterConfig.aggregations).map(function (v) {
//     newFilters[v] = [];
//   });
//   return newFilters;
// }

// export function getCategoryLabel(category) {
//   return category.title;
// }

// export function unselectCatOption(categoryName, tagOption) {
//   filters[categoryName] = filters[categoryName].filter(
//     (item) => item !== tagOption
//   );
// }

// export function getOptionLabel(option) {
//   return option.key + "(" + option.doc_count + ")";
// }

// export function getSearchResults() {
//   let result = itemsjsInstance.search({
//     per_page: 100,
//     // query: searchQuery,
//     filters: selectedFilters,
//     sort: "year_asc", // defined in filterConfig.sortings,
//     isExactSearch: true,
//   });
//   $emit("searchResultUpdated", result.data.items);
//   return result;
// }
