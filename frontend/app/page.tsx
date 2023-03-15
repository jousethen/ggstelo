import { Inter } from '@next/font/google'
import { Player } from '@/lib/types_be'
import { routes } from '@/lib/routes'
const inter = Inter({ subsets: ['latin'] })

export default async function Home() {
  const data = await getData()
  return (
    <main>
      <div>
        <ol>
          {data.results.map((d: Player, index: number) => {
            return <li key={index}>{d.gamer_tag} {d.elo}</li>
          })}
        </ol>
      </div>
    </main>
  )
}

export async function getData() {
  const response = await fetch(`${process.env.BASE_URL + routes.getPlayers.path}?page=1&page_size=50`)
  return response.json()
}