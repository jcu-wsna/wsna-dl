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
      @updatedSearch="
        (queryText) => {
          updateQueryTextAndSearch(queryText);
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
import itemsjsConfig from "components/query-config.json";
import libraryIndex from "components/library-index.json";
import DLFilterMenu from "components/filter-menu.vue";
import DLDocumentList from "components/document-list.vue";

let itemsjsInstance;

let selectedFilters = {};
let searchQuery = "";
const filteredDocs = ref([]);
let flatFilterList = ref([]);

function resetFilters() {
  // Generates a new filter object with each facet
  // having no items selected. Assigns this new object
  // to the global selectedFilters variable.
  var filters = {};
  Object.keys(itemsjsConfig.aggregations).map(function (facet) {
    filters[facet] = [];
  });
  selectedFilters = filters;
  flatFilterList.value = [];
}

function getDocList(fullDocList) {
  itemsjsInstance = itemsjs(fullDocList, itemsjsConfig);

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
  Object.keys(itemsjsConfig.aggregations).map(function (attrib) {
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

function updateQueryTextAndSearch(queryText) {
  searchQuery = queryText;
  filteredDocs.value = getDocList(libraryIndex);
  console.log(
    "librarypage: updateQueryTextAndSearch: selectedFilters(",
    selectedFilters,
    ")"
  );
}

resetFilters();
searchQuery = ""; // reset search text
filteredDocs.value = getDocList(libraryIndex);
</script>
