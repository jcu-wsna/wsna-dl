<template>
  <q-list>
    <!-- <p>{{ props.selectedFilters }}</p> -->
    <q-item>
      <q-input
        v-model="searchText"
        :value="searchText"
        filled
        type="search"
        hint="Search"
        autogrow
        counter
        maxlength="20"
        @keyup.enter="updatedSearch"
      >
        <template v-slot:after>
          <q-btn
            round
            dense
            flat
            icon="search"
            type="submit"
            @click="updatedSearch"
          />
        </template>
      </q-input>
    </q-item>
    <q-separator />
    <q-chip
      v-for="item in props.selectedFilters"
      :key="item"
      color="primary"
      text-color="white"
    >
      {{ item }}
    </q-chip>
    <q-separator />

    <DLFilterCategory
      v-for="[key, value] in Object.entries(props.filterCategories)"
      :categoryDetails="value"
      :key="key"
      @updatedFilter="
        (value1, value2) => {
          updatedFilter(value1, value2);
        }
      "
    />
  </q-list>
</template>

<script setup>
import { ref } from "vue";
import DLFilterCategory from "components/filter-category.vue";

const props = defineProps({
  filterCategories: Object,
  selectedFilters: Array,
});
const emit = defineEmits(["updatedFilter", "updatedSearch"]);

const searchText = ref("");

console.log("filter-menu: selectedFilters(", props.selectedFilters, ")");

function updatedFilter(cat, option) {
  // DEBUG
  console.log(
    "filter-menu: updatedFilter: category is (",
    cat,
    ") option selected is (",
    option,
    ")"
  );
  emit("updatedFilter", cat, option);
}

function updatedSearch() {
  searchText.value = searchText.value.trim();
  console.log("filter-menu: searchText(", searchText.value, ")"); // DEBUG
  emit("updatedSearch", searchText.value);
}
</script>
