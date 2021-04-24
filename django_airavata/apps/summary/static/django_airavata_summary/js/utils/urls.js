export default {
  editExperiment(experiment) {
    return (
      "/summary/experiments/" +
      encodeURIComponent(experiment.experimentId) +
      "/edit"
    );
  },
  navigateToEditExperiment(experiment) {
    window.location.assign(this.editExperiment(experiment));
  },
  experimentsList() {
    return "/summary/experiments";
  },
  navigateToExperimentsList() {
    window.location.assign(this.experimentsList());
  },
  viewExperiment(experiment, { launching = false } = {}) {
    return (
      "/summary/experiments/" +
      encodeURIComponent(experiment.experimentId) +
      "/" +
      (launching ? "?launching=true" : "")
    );
  },
  navigateToViewExperiment(experiment, { launching = false } = {}) {
    window.location.assign(
      this.viewExperiment(experiment, { launching: launching })
    );
  },
  createExperiment(appModule) {
    return (
      "/summary/applications/" +
      encodeURIComponent(appModule.appModuleId) +
      "/create_experiment"
    );
  },
  navigateToCreateExperiment(appModule) {
    window.location.assign(this.createExperiment(appModule));
  },
  editProject(project) {
    return "/summary/projects/" + encodeURIComponent(project.projectID) + "/";
  },
  projectsList() {
    return "/summary/projects";
  },
  navigateToProjectsList() {
    window.location.assign(this.projectsList());
  },
  storageDirectory(relativePath) {
    if (relativePath.startsWith("/")) {
      relativePath = relativePath.substring(1);
    }
    return "/summary/storage/~/" + relativePath;
  },
};
