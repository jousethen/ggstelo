// should correspond to value returned from backend route /players/{slug}
export interface Player {
  id: number
  slug: string
  gamer_tag: string
  elo: number
  highest_elo: number
  created_at: Date
  updated_at: Date
}