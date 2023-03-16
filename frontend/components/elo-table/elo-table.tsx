import type { EloTableProps } from "./interfaces";
import { Player } from "@/lib/types_be";
import styles from "./elo-table.module.css"

export default function EloTable({ tableData }: EloTableProps): JSX.Element {
  return (
    <table className={styles["elo-table"]}>
      <thead>
        <tr>
          <th>
            Rank
          </th>
          <th>
            Tag
          </th>
          <th>
            ELO
          </th>
          <th>
            Highest ELO
          </th>
        </tr>
      </thead>
      <tbody>
        {tableData.map((d: Player, index: number) => {
          return (
            <tr key={index}>
              <td className={styles["cell"]}>{index + 1}</td>
              <td className={styles["cell"]}>{d.gamer_tag}</td>
              <td className={styles["cell"]}>{d.elo}</td>
              <td className={styles["cell"]}>{d.highest_elo}</td>
            </tr>
          )
        })}
      </tbody>
    </table>
  );
}
