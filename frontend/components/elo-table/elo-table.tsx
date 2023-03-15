import type { EloTableProps } from "./interfaces";
import { Player } from "@/lib/types_be";
export default function EloTable({ tableData }: EloTableProps): JSX.Element {
  return (
    <table className="elo-table">

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
              <td>{index + 1}</td>
              <td>{d.gamer_tag}</td>
              <td>{d.elo}</td>
              <td>{d.highest_elo}</td>
            </tr>
          )
        })}
      </tbody>
    </table>
  );
}
