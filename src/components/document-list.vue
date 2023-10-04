<template>
  <div class="q-pa-md" style="max-width: 600px">
    <q-card flat
      ><p class="bg-accent">{{ docs.length }} Documents</p></q-card
    >

    <q-list dense bordered separator>
      <DLDocumentCard v-for="doc in docs" :docdata="doc" :key="doc.id" />
    </q-list>
  </div>
</template>

<style></style>

<script setup>
import DLDocumentCard from "components/document-card.vue";

defineProps({
  docs: Array,
});
</script>
