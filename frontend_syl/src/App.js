import { useState }from 'react'
import MenuSet from './Container/MenuSet';
import List from './Container/List'

const App = () => {
  const [company, setCompany] = useState(null)
  const [location, setLocation] = useState(null)
  const [level, setLevel] = useState(null)
  const [tag, setTag] = useState(null)
  const [yearAtCompamy, setYearAtCompany] = useState(9)
  const [yearTotal, setYearTotal] = useState(11)
  const [academicLevel, setAcademicLevel] = useState('Master')
  const [gender, setGender] = useState('male')
  const [race, setRace] = useState('Asian')
  const [compensation, setCompensation] = useState(276)
  const [base, setBase] = useState(148)
  const [stock, setStock] = useState(90)
  const [bonus, setBonus] = useState(38)
  const [check, setCheck] = useState(false)
  console.log(company)
  return <>
        <MenuSet setCompany={setCompany} setLocation={setLocation} 
                  setLevel={setLevel} setTag={setTag} setCheck={setCheck} 
                    company_name = {company} location_name = {location} level_name = {level}/>
        {check?<List company={company} location={location} level={level} tag={tag}/>:<></>}
  </>
  
}

export default App;
