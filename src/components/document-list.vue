<template>
  <div class="q-pa-md" style="max-width: 800px">
    <q-card flat>
      <p class="bg-accent">
        {{ docs.length }} Document{{ docs.length > 1 ? "s found" : " found" }}
      </p>
    </q-card>

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
