import { Method } from "./utils"

enum ApiRootType {
  BE = 'be',
  SELF = 'self',
}
const routes = {
  // Players
  getPlayers: {
    path: '/players',
    method: Method.GET,
    ApiRootType: ApiRootType.BE
  },
  getPlayer: {
    path: '/players/[slug]',
    method: Method.GET,
    ApiRootType: ApiRootType.BE
  },

}

export { routes }