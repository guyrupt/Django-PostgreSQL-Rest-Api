import '../App.css'
import { Space, Button } from 'antd'
import Companies from '../Component/Company'
import Locations from '../Component/Location'
import Levels from '../Component/Level'
import Tags from '../Component/Tag'

const MenuSet = ( { setCompany, setLocation, setLevel, setTag, setCheck , company_name, location_name, level_name} ) => {
    console.log(company_name)
    return (
        <div className='header'>
            <h1>SWE Explore</h1>
            <Space className='menu-set'>
                <div>
                    <div>Company</div>
                    <Companies setCompany={setCompany} setCheck={setCheck} />
                </div>
                <div>
                    <div>Location</div>
                    <Locations setLocation={setLocation} setCheck={setCheck} company = {company_name}/>
                </div>
                <div>
                    <div>Level</div>
                    <Levels setLevel={setLevel} setCheck={setCheck} company = {company_name} location = {location_name}/>
                </div>
                <div>
                    <div>Tag</div>
                    <Tags setTag={setTag} setCheck={setCheck} company = {company_name} location = {location_name} level = {level_name}/>
                </div>
                <Button onClick={()=>setCheck(true)}>Search</Button>
            </Space>
        </div>
    )

}

export default MenuSet
