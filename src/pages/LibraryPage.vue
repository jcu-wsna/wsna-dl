<template>
  <!-- DEBUG -->
  <!-- <p>good grief!</p> -->
  <!-- <p>{{ libraryIndex }}</p> -->
  <!-- <p>{{ filteredDocs }}</p> -->
  <!-- <p>filteredDocs.data.aggregations({{ filteredDocs.data.aggregations }})</p> -->
  <q-drawer
    show-if-above
    :width="250"
    :breakpoint="700"
    class="bg-secondary text-black"
  >
    <DLFilterMenu
      :filterCategories="filteredDocs.data.aggregations"
      :selectedFilters="flatFilterList"
      @updatedFilter="
        (facet, values) => {
          updateFiltersAndSearch(facet, values);
        }
      "
    />
  </q-drawer>

  <q-page padding>
    <DLDocumentList :docs="filteredDocs.data.items" />
    <!-- <p>sigh</p> -->
  </q-page>
</template>

<script setup>
import { ref } from "vue";
import itemsjs from "itemsjs";
import libraryIndex from "components/library-index.json";
import DLFilterMenu from "components/filter-menu.vue";
import DLDocumentList from "components/document-list.vue";

let itemsjsInstance;

//  selectedFilters:
//  keys are filter categories, values are lists of options in the category
//  that have been selected. Don't need to include categories with no
//  selections.
let selectedFilters = {};
const filteredDocs = ref([]);
let searchQuery = "";
let flatFilterList = ref([]);

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
  // text search will use these fields
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

function resetFilters() {
  // Generates a new filter object with each facet
  // having no items selected. Assigns this new object
  // to the global selectedFilters variable.
  var filters = {};
  Object.keys(filterConfig.aggregations).map(function (facet) {
    filters[facet] = [];
  });
  selectedFilters = filters;
  flatFilterList.value = [];
}

function getDocList(fullDocList) {
  itemsjsInstance = itemsjs(fullDocList, filterConfig);
  searchQuery = "";
  // DEBUG
  console.log("getDocList: selectedFilters.value - ", selectedFilters);

  let results = itemsjsInstance.search({
    per_page: 100,
    query: searchQuery,
    filters: selectedFilters,
    sort: "year_name_asc", // defined in filterConfig.sortings
    isExactSearch: true,
  });

  return results;
}

function updateFiltersAndSearch(facet, option) {
  // update selectedFilters and rerun the search
  Object.keys(filterConfig.aggregations).map(function (attrib) {
    if (attrib == facet) {
      if (option == undefined) {
        // we need to know what option has been removed
        // selectedFilters[facet] = selectedFilters[facet].filter(
        //   (item) => item !== option
        // );
        selectedFilters[facet] = [];
      } else {
        selectedFilters[facet] = option;
      }
    }
  });

  // update the flat list of filters to match the selectedFilters
  flatFilterList.value = [];
  Object.keys(selectedFilters).map(function (attrib) {
    flatFilterList.value.push(...selectedFilters[attrib]);
  });

  filteredDocs.value = getDocList(libraryIndex);
  console.log(
    "librarypage: updateFiltersAndSearch: selectedFilters(",
    selectedFilters,
    ")"
  );
}

resetFilters();
filteredDocs.value = getDocList(libraryIndex);
</script>
