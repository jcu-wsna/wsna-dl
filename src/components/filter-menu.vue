<template>
  <q-list>
    <!-- <q-item>{{ Object.entries(filterCategories)[0] }}</q-item> -->
    <!-- <p>{{ props.selectedFilters }}</p> -->
    <q-chip
      v-for="item in props.selectedFilters"
      :key="item"
      color="primary"
      text-color="white"
    >
      {{ item }}
    </q-chip>
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
import DLFilterCategory from "components/filter-category.vue";

const props = defineProps({
  filterCategories: Object,
  selectedFilters: Array,
});
const emit = defineEmits(["updatedFilter"]);

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
</script>
