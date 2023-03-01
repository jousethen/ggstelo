// should correspond to value returned from backend route /players/{slug}
export interface Player {
  id: number
  slug: string
  gamer_tag: string
  elo: number
  highest_elo: number
  matches: Match[]
  created_at: Date
  updated_at: Date
}

export interface Match {
id: number
player1: Player
player1_score: number
player2: Player
player2_score: number
player1_elo_change: number
player2_elo_change: number
tournament: Tournament
created_at: Date
updated_at: Date
}

export interface Tournament {
  name: string
  slug: string
  matches: Match[]
  created_at: Date
  updated_at: Date
}