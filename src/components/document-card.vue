<template>
  <!-- DEBUG-->
  <!-- <p>{{ docdata }}</p> -->
  <q-expansion-item
    expand-separator
    :label="docdata.Title"
    :icon="docdata.icon"
    :href="docdata.URL"
    target="_blank"
  >
    <q-card-section>
      <q-item-label
        v-for="[key, value] in getDocDetails(docdata)"
        :label="key"
        :value="value"
        :key="key"
      >
        <b>{{ key }}:</b> {{ value }}
      </q-item-label>
    </q-card-section>
  </q-expansion-item>
</template>

<script setup>
defineProps({ docdata: Object });

function getDocDetails(obj) {
  let details = Object.entries(obj);
  return details;
}
</script>
