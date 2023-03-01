const {
  generateTemplateFiles,
  generateTemplateFilesBatch,
} = require("generate-template-files");

generateTemplateFiles([
  {
    option: "Create A New Component",
    defaultCase: "(kebabCase)",
    entry: {
      folderPath: "./lib/new-component-ts/",
    },
    stringReplacers: ["__title__"],
    output: {
      path: "./components/__title__",
      pathAndFileNameDefaultCase: "(kebabCase)",
    },
    onComplete: (results) => {
      const title = results.stringReplacers[0].slotValue;
      generateTemplateFilesBatch([
        {
          option: "Add New Component Styles",
          defaultCase: "(kebabCase)",
          entry: {
            folderPath: "./lib/new-component-styles/__title__.module.css",
          },
          dynamicReplacers: [{ slot: "__title__", slotValue: title }],
          output: {
            path: `./components/__title__/__title__.module.css`,
            pathAndFileNameDefaultCase: "(kebabCase)",
          },
          onComplete: (results) => {
            console.log(`results`, results);
          },
        },
      ]).catch(() => {
        console.error("Build Error");
      });
    },
  },
]);
