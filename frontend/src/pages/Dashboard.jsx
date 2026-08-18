import Navbar from "../components/Navbar";
import StatCard from "../components/StatCard";
import RiskChart from "../components/RiskChart";
import StudentTable from "../components/StudentTable";

function Dashboard() {
  return (
    <>
      <Navbar />

      <main>
        <h1>IRIS Dashboard</h1>
        <p>Intelligent Risk Identification System</p>

        <section>
          <StatCard title="Total Students" value="120" />
          <StatCard title="High Risk" value="18" />
          <StatCard title="Medium Risk" value="32" />
          <StatCard title="Low Risk" value="70" />
        </section>

        <RiskChart />

        <StudentTable />
      </main>
    </>
  );
}

export default Dashboard;
