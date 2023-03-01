import { Inter } from '@next/font/google'
import styles from './page.module.css'
import { Player } from '@/lib/types_be'
import { routes } from '@/lib/routes'
const inter = Inter({ subsets: ['latin'] })

export default async function Home() {
  const data = await getData()
  return (
    <main className={styles.main}>
      <div className={styles.description}>
        <p>
          Get Players
        </p>
        <ol>
          {data.map((d: Player, index: number) => {
            return <li key={index}>{d.gamer_tag} {d.elo}</li>
          })}
        </ol>
      </div>
    </main>
  )
}

export async function getData() {
  const response = await fetch(`${process.env.BASE_URL + routes.getPlayers.path}`)
  return response.json()
}