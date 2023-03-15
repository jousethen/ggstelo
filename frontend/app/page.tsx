import { Inter } from '@next/font/google'
import { Player } from '@/lib/types_be'
import { routes } from '@/lib/routes'
import EloTable from '@/components/elo-table/elo-table'
const inter = Inter({ subsets: ['latin'] })

export default async function Home() {
  const data = await getData()
  return (
    <main>

      <EloTable tableData={data.results} />
    </main>
  )
}

export async function getData() {
  const response = await fetch(`${process.env.BASE_URL + routes.getPlayers.path}?page=1&page_size=50`)
  return response.json()
}